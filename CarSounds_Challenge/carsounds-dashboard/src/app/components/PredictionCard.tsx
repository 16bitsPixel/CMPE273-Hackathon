import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';

interface CardParams {
    predictedclass: string;
    confidence: number;
}

const images = {
    "pump": "https://autoimage.capitalone.com/cms/Auto/assets/images/1095-hero-fuel-pump-replacement-101.jpg",
    "fan": "https://www.howacarworks.com/illustration/659/how-the-fan-is-fitted.png",
    "gearbox": "https://cdn.autodoc.de/uploads/info_section/article/57/1704801709_2685_2255e79cc772bf3363ff4dde1e462184.jpeg",
    "valve": "https://www.howacarworks.com/illustration/86/finger-operated-ohc.png"
};

export default function PredictionCard({predictedclass, confidence}: CardParams) {
    return (
        <Card sx={{ maxWidth: 345, marginTop: "1%" }}>
          <CardActionArea>
            <CardMedia
              component="img"
              height="200"
              image={images[predictedclass]}
            />
            <CardContent>
              <Typography gutterBottom variant="h5" component="div">
                {predictedclass}
              </Typography>
              <Typography variant="body2" sx={{ color: 'text.secondary' }}>
                Confidence Rating: {confidence}
              </Typography>
            </CardContent>
          </CardActionArea>
        </Card>
    );
}